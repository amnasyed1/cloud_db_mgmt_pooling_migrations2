# cloud_db_mgmt_pooling_migrations2

## 1. Connection Pooling Setup: 

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


## Documentation and Error Handeling
An error I got in the process was my .gitignore file not working when I pushed the Azure content onto Github. The .gitignore file pushed properly for when I was doing the GCP steps, but not for Azure. Therefore, I did everything over in a new repo and then made sure the .gitignore file was working and then pushed it into this new repo. I then deleted the original repo because it would have leaked information.  
