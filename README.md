<div id="top" align="center">
  <img src="https://img.shields.io/github/contributors/howstrangeoficial/flask-deploy?style=for-the-badge" />
  <img src="https://img.shields.io/discord/928742162219270175?color=blue&label=Discord&style=for-the-badge" />

  <br />

  <a href="https://github.com/howstrangeoficial">
    <img src="images/heroku.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Deploy Flask Heroku</h3>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Here I am teaching you how to make a python application on the web using the inclivel micro framework that is flask, I will teach you how to deploy on the heroku platform which is free.

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* python virtual env
  ```sh
  python -m venv venv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/howstrangeoficial/flask-deploy.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Deploy Heroku

1. Login Heroku
    ```sh
    heroku login
    ```
2. Create App repo
    ```sh
    heroku create projectname
    ```
3. Push to remote heroku branch main
    ```sh
    git push heroku main
    ```
4. Now Deployment
    ```sh
    heroku ps:scale web=1
    ```
5. Open App link
    ```sh
    heroku open
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples heroku deploy [Documentation](https://devcenter.heroku.com/categories/reference)_

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the Public License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
