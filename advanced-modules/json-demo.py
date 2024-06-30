import json
import os.path


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []  # Kullanıcılar bu listede tutulacak.
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from
        self.loadUsers()  # users.json dosyasındaki kullanıcıları users listesine ekler.

    def loadUsers(self):
        if os.path.exists('users.json'):  # Dosya fiziksel olarak var mı kontrol.
            with open('users.json', 'r', encoding='utf-8') as f:  # Dosyayı okuma modunda açar.
                loadable_users = json.load(f)  # users.json dosyasındaki veriyi okur ve loadable_users listesine ekler
                for item in loadable_users:
                    item = json.loads(item)  # string olarak okunup eklenen veriyi dict yapısıma çevirir
                    # User class'ından bir instance oluşturup new_user değişkenine atar.
                    new_user = User(username=item['username'], password=item['password'], email=item['email'])
                    self.users.append(new_user)  # döngü ile dönüşen her yeni kullanıcıyı users listesine ekler

    def register(self, user_to_add: User):
        self.users.append(user_to_add)
        print('Kullanıcı başarıyla oluşturuldu.')
        self.savetoFile()

    def login(self, username, password):
        for user_to_login in self.users:
            if user_to_login.username == username and user_to_login.password == password:
                self.isLoggedIn = True
                self.currentUser = user_to_login
                print('Kullanıcı Girişi Başarılı!')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Kullanıcı Çıkışı Başarılı!')

    def identity(self):
        if self.isLoggedIn:
            print(f'{self.currentUser.username} kullanıcısı sisteme giriş yapmış durumda.')
        else:
            print('Herhangi bir kullanıcı girişi yapılmadı.')

    def savetoFile(self):
        user_list = []

        for user_to_save in self.users:  # users listesindeki mevcut kullanıcıları döner
            user_list.append(json.dumps(
                user_to_save.__dict__))  # her bir kullanıcı kaydını user_list'e dict yapısına dönüştürerek ekler

        with open("users.json", "w") as f:  # users.json dosyasını yazma modunda açar
            json.dump(user_list, f)  # user_list listesindeki tüm kullanıcı bilgilerini users.json dosyasına yazar.


repository = UserRepository()  # UserRepository'den bir instance alır. Kullanıcılar bu repository ile işlem görecek.

while True:
    print(" Menü ".center(50, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            # register
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user = User(username=username, password=password, email=email)
            repository.register(user)
        elif secim == '2':
            # login
            if repository.isLoggedIn:
                print('Sisteme giriş yapılmış durumda')
            else:
                username = input('username: ')
                password = input('password: ')

                repository.login(username=username, password=password)
        elif secim == '3':
            # logout
            repository.logout()
        elif secim == '4':
            # display username
            repository.identity()
        else:
            print('Hatalı bir seçim yaptınız!')
