def get_all_users_age(total_users=1000):
    age = []
    for id in range(total_users):
        user = access_db_to_get_users_by_id(id)
        age.append([user.name, user.age])
    return age

total_users = 1000000000
info = get_all_users_age(total_users)
for user in info:
    print(user)
