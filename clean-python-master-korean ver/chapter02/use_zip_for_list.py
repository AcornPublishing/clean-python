def get_user_salary_info():
    users = get_users_name_from_db()
    # ["Abe", "Larry", "Adams", "John", "Sumit", "Adward"]
    
    users_salary = get_users_salary_from_db()
    #  ["2M", "1M", "60K", "30K", "80K", "100K"]

    users_salary = []
    for index in range(len(users)):
        users_salary.append([users[index], users_salary[index]])

    return users_salary
    
