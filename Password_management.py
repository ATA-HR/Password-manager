import sqlite3, pyperclip

from password_generator import pass_gen


while True:
    print('''
        Menu
        1.Generate new password
        2.Save a password
        3.Exit
        ''')
    choice = int(input('Select a option:'))

    if choice == 1:
        password = pass_gen()
        pyperclip.copy(password)
        print(f'Your password seccusfully generated. --> {password}')
        print('Your password copied in clipboard.')

    elif choice == 2:    
        con = sqlite3.connect('password_manager.db')
        cur = con.cursor()
        try:
            cur.execute('CREATE TABLE password(title, password)')   
        except:
            pass
        name = input('enter name:')
        cur.execute(f'''
            INSERT INTO password VALUES ('{name}', "{password}")
        ''')
        con.commit()

    elif choice == 3:
        exit()

    if input('Do you want to continue?(y/n)') == 'n':
        break