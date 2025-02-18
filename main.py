from controllers import Application
import os

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/tournaments"):
    os.makedirs("data/tournaments")


application = Application()

application.display_menu()
