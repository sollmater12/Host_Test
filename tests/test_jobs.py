from requests import post, delete



# удачный запрос
print(post('http://localhost:5000/api/update_job/110',
           json={'id': 3, 'team_leader': 1, 'job': 'Помочь', 'work_size': 8, 'collaborators': '4, 5', }).json())
# указан несуществующий id
print(post('http://localhost:5000/api/update_job/110',
           json={'id': 3, 'team_leader': 1, 'job': 'Помочь', 'work_size': 7, 'collaborators': '4, 5', }).json())
# указаны не все параметры
print(post('http://localhost:5000/api/update_job/3',
           json={'id': 3, 'team_leader': 1, 'work_size': 7, 'collaborators': '4, 5', }).json())