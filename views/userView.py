class UserView():
    def display_users(self, users):
        col_widths = [15, 15, 20, 12]

        print("\n - Liste de tous les utilisateurs - \n")

        header = f"{'Nom':<{col_widths[0]}} {'Prénom':<{col_widths[1]}} {'Date de naissance':<{col_widths[2]}} {'ID National':<{col_widths[3]}}"
        print(header)
        print("=" * len(header))

        for user in users:
            print(f"{user.surname:<{col_widths[0]}} {user.name:<{col_widths[1]}} {user.dateOfBirth:<{col_widths[2]}} {user.nationalID:<{col_widths[3]}}")
