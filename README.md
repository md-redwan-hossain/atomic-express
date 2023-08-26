## atomic-express: Modular ExpressJS Project Structure Generator with Typescript

### Structure explanation:

- The structure is divided into `macro` and `micro` directory.
- In `macro`, all the reuseable stuffs are wrrien.
- `micro` contains individual modules that are independent and reuse code from `macro`
- Example, for a blog management system, `micro` can possibly contain `user`, `content` module while `macro` can contain reuseable validation logics.


### Features:
- Full project setup
- Create micro module inside current express project


**Make sure python, node JS, NPM are installed in your system.**

**For directly running from terminal, you can use bash aliasing by the following command:**
<br>

`curl -O --output-dir "$HOME" https://raw.githubusercontent.com/md-redwan-hossain/atomic-express/main/atomic-express.py && echo 'alias atomic-express="python3 $HOME/atomic-express.py"' >>~/.bashrc && source ~/.bashrc`

**Now just type `atomic-express` in the terminal to use atomic-express.**


