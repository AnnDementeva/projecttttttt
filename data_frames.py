__all__= ['create_data_frame', 'sorted_df_type']
from glob import glob
from pathlib2 import Path
import pandas as pd

def create_data_frame(choise, folders):
    """Функция считывает данные из директории 
    и на выбор (choise) создает датафреймы events (в которой находятся данные кальцевых активностей) 
    и датафрейм images (в которой находятся данные кальцевых событий),
    folders - путь до директории с данными,
    возвращаемое значение - data frame, в котором 
        столбец 1 (image_name) - имя изображения, 
        столбец 2 (time) - момент времени, в ходе которого было сделано изображение,
        столбец 3 (type) - папка, откуда было взято изображение,
        столбец 4 (file_path) - путь до изображения """
    current_dir = Path.cwd() #текущая директория
    data_path = current_dir / folders
    if choise == 'event':
        astrocytes_mask = current_dir / folders / '**'/ '**' / '**' / 'event*.png' 
    elif choise == 'image':
        astrocytes_mask = current_dir/ folders / '**'/ '**' / '**' / 'smoothed*.png' 

    file_names = glob(str(astrocytes_mask))

    image_names = []
    time = []
    type = []
    file_paths = []
    n = []
    type = []

    for file_name in file_names:
        file_path = Path(file_name)
        name = file_path.stem
        name_parts = name.split('_t')   
        times = name_parts[1]
        image_name = file_path.relative_to(data_path)
        file_paths.append(file_path)
        image_names.append(image_name)
        time.append(int(times)+1000)
        name=file_name.split('\\')
        namee=name[7].split('-')
        n.append(name[7])
    unique = list(set(n))
    for i in range(len(n)):
        for j in range(len(unique)):
            if n[i] == unique[j]:
                type.append(unique[j])
            else:
                continue

    df_astrocytes = pd.DataFrame({
        'image_name': image_names, 
        'time': time, 
        'types': type,
        'file_path': file_paths
    })
    return df_astrocytes

def sorted_df_type(df_main, type):
    """Функция принимает на вход data frame, 
    который будет сортировать и разбивать на новые data frames 
    (количество data frames зависит от количества папок (types)).
    В итоге можем получить исходя из нашей задачи 6 новых data frames, в которых
        столбец 1 (image_name) - имя изображения, 
        столбец 2 (time) - момент времени, в ходе которого было сделано изображение,
        столбец 3 (type) - папка, откуда было взято изображение,
        столбец 4 (file_path) - путь до изображения"""
    unique = df_main.types.unique()
    for i in range(len(unique)):
        if type == unique[i]:
            df_type= df_main[df_main.types.str.startswith(type)]
        else:
            continue
    df_type = df_type.sort_values(by='time')
    df_type['time'] = df_type['time'].apply(lambda x: x - 1000)
    return df_type