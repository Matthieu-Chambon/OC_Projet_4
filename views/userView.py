class UserView():
    def display_users(self, users):
        col_widths = [5, 15, 15, 20, 12]

        print("\n - Liste de tous les utilisateurs - \n")

        header = f"{'N°':<{col_widths[0]}} {'Nom':<{col_widths[1]}} {'Prénom':<{col_widths[2]}} {'Date de naissance':<{col_widths[3]}} {'ID National':<{col_widths[4]}}"
        print(header)
        print("=" * len(header))

        for index, user in enumerate(users, start=1):
            print(f"{index:<{col_widths[0]}} {user.surname:<{col_widths[1]}} {user.name:<{col_widths[2]}} {user.dateOfBirth:<{col_widths[3]}} {user.nationalID:<{col_widths[4]}}")
