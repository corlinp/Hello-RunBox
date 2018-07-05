## The Tenzar RunBox dashboard

While the examples in this repo use the RunBox CLI, you can also run most examples directly from the [RunBox Dashboard](https://run.tenzar.com/deployments).

Here's an example of hello world in Julia using only the RunBox dashboard:

1. Import the image

Navigate to the 'import' page under 'console' on the left side bar. From there, enter the Docker Hub tag and an image name to import it as.

![import image](https://user-images.githubusercontent.com/5972540/42342349-ac4e4f6a-804a-11e8-90fd-e377d163ac54.png)

2. Import the script

Back on the import page, choose 'from Volume'. The script can be imported directly from GitHub with the link:  https://raw.githubusercontent.com/corlinp/Hello-RunBox/master/Julia/hello_world.jl

![import script](https://user-images.githubusercontent.com/5972540/42342419-dc44af16-804a-11e8-98d4-d6ab2f89666b.png)

3. Run a deployment

Navigate to 'deploy' on your console and select the julia image and the volume containing your code.

![run deployment](https://user-images.githubusercontent.com/5972540/42342136-1f99775c-804a-11e8-9bef-95e7227cba9f.png)

4. Monitor your deployment

Monitor the status of your deployment on the 'My Deployments' page until it's 'Running'.

![monitor](https://user-images.githubusercontent.com/5972540/42342477-0badf1fe-804b-11e8-9a18-31b8ea2aa5f2.png)

5. Use the web shell

Click on your deployment and navigate to the 'shell' tab.

![image](https://user-images.githubusercontent.com/5972540/42342551-46294b1c-804b-11e8-9d9e-3d869dedb2ee.png)

6. Run your code

Simply type `julia hello_world.jl` into the box and hit enter.

![image](https://user-images.githubusercontent.com/5972540/42342643-8dcc5676-804b-11e8-83e2-520f74d3110a.png)


You're done! Now feel free to play around and destroy your deployment from the My Deployments page.
