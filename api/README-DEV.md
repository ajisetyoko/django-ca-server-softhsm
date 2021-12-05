## Setup Django + Database (Local)
### Create Project
- Install requirepments
```pip install -r requirepments.txt```
- Make Django Project
```django-admin startproject service```
- Make Django Apps
  - ```user_management``` will be use to manage the user
  - ```softhsm_client``` will be use to operate with **softhsm2** apps
    ```
    cd service
    python manage.py startapp user_management
    python manage.py startapp softhsm_client
    ```

#### Additional Setting
- Setting ```user_management``` - TBD
- Setting ```softhsm_client```
  -  Add the apps to django project setting
  -  Add url to to django project url
  -  Setting the apps url
  -  Add rest_framework to the installed apps in project setting
- Test


## 