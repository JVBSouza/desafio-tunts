<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h2 align="center">Tunts Challenge </h2>
  <p align="center">
    Developed by: José Vinícius Boing de Souza.

  </p>
</p>
<br />

## Challenge:
This project was developed for the Tunts internship challenge to demonstrate the candidates programming skill.
With Python, a simple application was developed that connects to google sheets, reads the data and updates cell values. 

## Developed with:
* [Python](https://www.python.org/)

## Google Spreadsheet
  The following google spreadsheet was used in the applicaton.
  ```sh
  https://docs.google.com/spreadsheets/d/1ZgYaU1_9VeyTdQpUgDW3HqCSnJxuiN8Z65q1y5K0RKQ/edit?usp=sharing
  ```
## Instalation and execution
  1. Clone or download this repository. <br>
  2. Install the following packages with PIP:
  ```sh
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```
  3. This application requires a Google Cloud Plataform server. Follow this link: 
  https://developers.google.com/workspace/guides/create-project <br>
  for creating and enabling the API.  <br>
  4. A credential is also required. Follow the steps described in this link: 
  https://developers.google.com/workspace/guides/create-credentials <br>
  for creating and downloading it. Rename the file as "credentials.json". <br>
  5. A test user must be allowed in the Google CLoud Plataform. Add a google account to authorize the application connection to the server.
  6. Run the application:
  ```sh
  python sheetUpdate.py  
  ```

## Contact
Developer: José Vinícius Boing de Souza </br>
E-mail: joseboing@gmail.com
