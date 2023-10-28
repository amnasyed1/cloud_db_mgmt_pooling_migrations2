# cloud_db_mgmt_pooling_migrations2

## Connection Pooling Setup: 

**Azure:** Spinning up an Azure MySQL Database instance

1. Once logged into Microsoft Azure, go to `Azure Database for MySQL servers`.
2. Click `Create` and select `Flexible server` and then click `Create` again.
3. Under **`Server details`** ensure your subscription is correct, and either select a previously created resource group or create a new one.
4. Create a `Server name` and under **`Compute + storage`** change `compute size` to `Standard_B1s (1 vCore, 1GiB memory, 400 max iops` and click `Save`.
5. Under **`Authentication`** create an `Admin username` and `Password`, then click **`Next: Networking`**.
6. Under **`Firewall rules`** click `Add 0.0.0.0 - 255.255.255.255` and `Add current client IP address` and then click **`Review + create`** and then **`Create`**.
7. Once the instance is deployed, under Settings on the left hand-side click `Server parameters` change `max_connections` to `20` and `connnect_timeout` to 3. 



**GCP:** Creating a Google Cloud SQL MySQL instance

1. Once logged into console.cloud.google.com, ensure you are in the correct resource. After that click navigation menu (the hamburger icon on the top left corner) and click `SQL`.
2. Click `Create Instance` on the top of the screen, and click `Choose MySQL`.
3. Under **`Instance info`** create an `Instance ID` and `Password`.
4. Under **`Choose a Cloud SQL edition`** select `Enterprise` and change the preset to `Sandbox`.
5. Under **`Customise your instance`** click on `Show configuration options` and click on `Machine configuration` and change the machine shapes to `Shared core` and `1 vCPU, 0.614 GB`. Next, click on `Connections` and click `Add a network`. Name it `Allow-All` and set the network as `0.0.0.0/0`. Then click **`Create Instance`**. 

## Database Schema Structure and Rational

My databases contained 2 tables, **Patients** and **Allergy Testing**. The **Patients** table had 5 fields: ID, First Name, Last Name, Date of Birth, and Gender. The Primary Key in the table was `ID`. The **Allergy Testing** table also had 5 fields: ID, Patient ID, Test Name, Test Result, and Test Date. The Primary Key in the table was `ID`, and the Foreign Key was `Patient ID`. 

I launched MySQL Workbench and connected my GCP and Azure Instances, seperately. I utiilized the `reverse engineer` function to generate an ERD for my database for a visualization of the database schema structure. I included the screenshot of the diagram in the `screenshots` folder above. 

## Database Migrations with Alembic

1. Navigate to the folder you want to preform the database migrations with alembic (for instance, navigate to your Azure or GCP folder). Once you are in your desired folder, in the terminal in Google Cloud Shell type `alembic init migrations` and hit enter
2. Then navigate to the **`alembic.ini`** file under the newly created migrations folder. In the alembic.ini file, go to line 63 and change the command to `sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name`, and replace with your own credentials.
3. In your .gitignore file, include `alembic.ini`, to ensure your sensitive information will be protected.
4. Locate the **`env.py`** file, also in the migrations folder. Remove `#` for lines 19 and 20. In line 19, change the command to say `from <your py file name> import Base` and in line 20 to say `target_metadata = Base.metadata`.
5. Then to create a migration type `alembic revision --autogenerate -m "create tables"` in the terminal.
6. Next, to run the migration type `alembic upgrade head`.
7. Lastly, to save type  `alembic upgrade head --sql > migration.sql`.

## Error Handling
I ran into quite a few errors throughout this assignment. When working on the Flask integration, I pushed changes onto Github and my .env file and .gitignore file did not work properly and my sensitive information was not protected. I then transferred all my error-free work into this new repo, and started over. When I did it for a second time, I triple-checked everything so the same mistake would not happen again before pushing the updates into the repo, as well as when I was adding `alembic.ini` to the .gitignore file later on in the assignment. I also recieved an error pertaining to the allergy_testing table apparently not existing when I had created and populated it in Cloudshell and knew it was there. I then logged into mySQL from the terminal, and kept doing the commands `show tables;` and `SELECT * FROM allergy_testing`. It was all working, I was confused as to why the Flask app then was not working. When I went back to do it again a few times later, I realized the table name I had created was not `allergy_testing`, but `allergy_tests`. Once I isolated what the problem was, everything else ran smoothly.  


