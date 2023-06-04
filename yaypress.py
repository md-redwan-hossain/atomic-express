import os
import shutil

def install_pip() -> None:
    print("\nPython Package Manager(pip) is missing! Installing...\n")
    os.system("sudo -S apt install python3-pip -y")


install_pip() if not shutil.which("pip") else None

PIP_PACKAGE_NEEDED_COUNT = 2
PIP_PACKAGE_AVAILABLE_COUNT = 0

try:
    from clint.textui import colored
    PIP_PACKAGE_AVAILABLE_COUNT += 1
except ModuleNotFoundError:
    print("\nDependency missing -> clint. Installing...\n")
    os.system("pip3 install clint")


try:
    import wget
    PIP_PACKAGE_AVAILABLE_COUNT += 1
except ModuleNotFoundError:
    print("\nDependency missing -> wget. Installing...\n")
    os.system("pip3 install wget")

if PIP_PACKAGE_AVAILABLE_COUNT != PIP_PACKAGE_NEEDED_COUNT:
    print("\nRelaunch yayjs again to load the installed dependencies...")
    exit()



class YayPress:
    def __init__(self) -> None:
        self.BASE_DIR = os.path.abspath(os.getcwd())

        self.ESLINT_NODE_CONFIG_URL = "https://gist.githubusercontent.com/md-redwan-hossain/ff27ae60a59b20cefc4217e3fa59e663/raw/3bca1e9e7d66156566844d2bf63ccafa60665507/.eslintrc.json"

        self.TS_CONFIG_URL = "https://gist.githubusercontent.com/md-redwan-hossain/5ab953334fa85cf6f687f6f39b9826ca/raw/e33374de4377b55a90f2557e50b9bb8647cb4272/tsconfig.json"

        self.TS_GLOBAL_TYPE_FILE_URL = "https://gist.githubusercontent.com/md-redwan-hossain/87ccf85a1558a59d65b2cf6359ec8a42/raw/159ce57faab98cf388a50c40e2007a80ed354ff4/globalTypes.d.ts"


    def empty_dir_checker(self):
        if os.listdir(self.BASE_DIR):
            print(colored.red("Directory is not empty. Run YayPress inside an empty directory."))
            exit()
        else:
            pass


    def list_menu_input_handler(self) -> int:
        while True:
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print(colored.red("Invalid input. Try again"))
            else:
                return choice


    def list_menu(self) -> int:
        print("\n")
        print(colored.yellow("YayPress: Modular ExpressJS Project Structure Generator with Typescript"))
        print(colored.green("1. Full project setup"))
        print(colored.green("2. Create micro module inside current express project"))
        print(colored.red("0. Exit"))
        choice = self.list_menu_input_handler()
        return choice


    def micro_module_creator_prompter(self):
        while True:
            print("\n")
            print(colored.yellow("Do you want to create a micro module? (y/n)"),end=" ")
            micro_module_creation_choice = input()
            if(micro_module_creation_choice not in ["y","n"]):
                print(colored.red("Invalid Input. Try again..."))
            else:
                break

        if(micro_module_creation_choice=="y"):
            self.micro_module_creator()


    def download_eslint_node_config(self) -> None:
        if (os.path.exists(f"{self.BASE_DIR}/.eslintrc.json")):
            os.remove(f"{self.BASE_DIR}/.eslintrc.json")
        wget.download(self.ESLINT_NODE_CONFIG_URL, f"{self.BASE_DIR}/.eslintrc.json")


    def download_ts_config(self) -> None:
        if (os.path.exists(f"{self.BASE_DIR}/tsconfig.json")):
            os.remove(f"{self.BASE_DIR}/tsconfig.json")
        wget.download(self.TS_CONFIG_URL, f"{self.BASE_DIR}/tsconfig.json")


    def download_ts_global_type_file(self) -> None:
        if (os.path.exists(f"{self.BASE_DIR}/src/globalTypes.d.ts")):
            os.remove(f"{self.BASE_DIR}/src/globalTypes.d.ts")
        wget.download(self.TS_GLOBAL_TYPE_FILE_URL, f"{self.BASE_DIR}/src/globalTypes.d.ts")


    def file_creator(self,file_path:str)-> None:
        try:
            open(file_path, "w").close()
        except OSError as err:
            print(err)


    def write_in_file(self,file_path:str,text_to_write:str)-> None:
        try:
            with open(f"{self.BASE_DIR}/{file_path}", "a") as file:
                file.write(f"{text_to_write}")
        except OSError as err:
            print(err)


    def folder_creator(self,folder_path:str)-> None:
        try:
            if os.path.exists(f"{self.BASE_DIR}/{folder_path}"):
                shutil.rmtree(f"{self.BASE_DIR}/{folder_path}")
            os.mkdir(f"{self.BASE_DIR}/{folder_path}")
        except OSError as err:
            print(err)


    def micro_module_creator(self)-> None:
        if not os.path.exists(f"{self.BASE_DIR}/src"):
            print(colored.red("src directory doesn't exists. Create a project structure first."))
            return
        micro_module_name = input("Enter micro module name: ")
        self.folder_creator(f"src/micro/{micro_module_name}")
        micro_files = [f"routes.{micro_module_name}.ts",f"models.{micro_module_name}.ts",f"controllers.{micro_module_name}.ts",f"validators.{micro_module_name}.ts",f"middlewares.{micro_module_name}.ts",f"events.{micro_module_name}.ts"]
        for file in micro_files:
            self.file_creator(f"{self.BASE_DIR}/src/micro/{micro_module_name}/{file}")
        print(colored.green("DONE"))


    def macro_level_creator(self)-> None:
        macro_files = ["server.ts","macro/settings.macro.ts","macro/errorHandler.macro.ts","macro/routes.macro.ts","macro/roleGuard.macro.ts","macro/validators/auth.validator.macro.ts","macro/middlewares/auth.middleware.macro.ts","macro/utils/jwt.util.macro.ts"]
        necessary_folders = ["src","src/macro","src/micro","src/macro/validators","src/macro/middlewares","src/macro/utils"]
        for folder in necessary_folders:
            self.folder_creator(folder)
        for file in macro_files:
            self.file_creator(f"{self.BASE_DIR}/src/{file}")

        self.file_creator(f"{self.BASE_DIR}/README.md")



    def express_with_ts_full_setup(self) -> None:
        self.empty_dir_checker()
        os.system("npm init -y")
        os.system('npm pkg set type="module"')
        os.system('npm pkg set scripts.dev="NODE_ENV=development nodemon --esm --files ./src/server.ts"')
        os.system('npm pkg set scripts.build="npx tsc"')
        os.system("npm i express express-validator cookie-parser http-errors multer helmet jsonwebtoken dotenv bcrypt cors mongoose morgan nodemailer node-cache rate-limiter-flexible validator luxon")
        os.system("npm i -D typescript ts-node nodemon @types/node @types/express @types/cookie-parser @types/jsonwebtoken @types/bcrypt @types/cors @types/morgan @types/nodemailer @types/http-errors @types/luxon @types/multer eslint-import-resolver-typescript @types/validator")
        os.system("npm i -D eslint typescript prettier eslint-config-prettier eslint-plugin-prettier eslint-plugin-import @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-config-airbnb eslint-config-airbnb-typescript eslint-plugin-promise eslint-plugin-n eslint-import-resolver-typescript")
        self.macro_level_creator()
        self.download_ts_global_type_file()
        self.download_ts_config()
        self.download_eslint_node_config()
        self.file_creator(".env")
        self.file_creator("sample.env")
        self.file_creator(".gitignore")
        gitignore_texts = ["node_modules","\n.env","\ndist"]
        env_texts = ["SERVER_PORT=","\nSERVER_IP=","\nJWT_SECRET=","\nMONGODB_URL="]
        readme_texts = ["This project is scaffolded by [YayPress](https://github.com/md-redwan-hossain/yaypress)","\n\nStart development server: `npm run dev`", "\n\nTranspile project ((TS -> JS): `npm run build`"]

        for text in gitignore_texts:
            self.write_in_file(".gitignore",text)

        for text in env_texts:
            self.write_in_file(".env",text)
            self.write_in_file("sample.env",text)

        for text in readme_texts:
            self.write_in_file("README.md",text)



    def navigation(self) -> None:
        try:
            while True:
                choice_input = self.list_menu()
                match choice_input:
                    case 0:
                        print(colored.blue("\nBYE..."))
                        break
                    case 1:
                        self.express_with_ts_full_setup()
                    case 2:
                        self.micro_module_creator()


        except KeyboardInterrupt:
            print(colored.blue("\nBYE..."))


if __name__ == "__main__":
    yay = YayPress()
    yay.navigation()
