# immfly-backend-test
Media platform API backend test.

I'm attending to an online course of Advanced REST API Backend Development at London App Development School that really helped me on doing this technical test and also another course of Test Driven Development that I've just started and that also help me with some simple test development I'm not yet very familiarized with.

I've started the project by creating a GitHub-project defining its dependencies and requirements, as well as a
-DockerFile to define the steps needed to build a docker image as the image version (alpine 3.17), the dependencies defined on requirement.txt and the RUN command to build the docker image.
-DockerIgnore to indicate what to be excluded from the image like the python cache files created automaticaly.
-main folder "app" of the project where all the files and folders are contained.

All the tests, linting, and folders created was made/run via terminal with the command defined on the docker-compose.yml file, as well as the migrations. (with "startapp" and "makemigrations").
This was tought on the very first classes of the course I'm attending.

I've tried to develop a "checks.yml" file at github/workflows to help me automate my tests and lintings with the GitHub Actions, but for some reason I do not know yet why it's not working, I guess there is something related with the version of the image, or the python version or the docker-compose version. At this point all the git commit/push and the tests and lintings were made manually via terminal (using the git commands and docker-compose).

The management rating command took me a bit of time to get it done searching information and reading the django documentation to learn more about foreignkey and many-to-many relations (this was the very first time I've heard about it), and once I've got it, I found myself stucked at the development of its unit test even though I could code some tests to check the creation of Contents and Channels objects. Because I could not yet write a test for the management command I'm not very convinced that it is working properly.

There are some empty tests in "test_models" file that test if the creation of contents and/or subchannels in a channel with subchannels/contents raises an error. I'm not yet have any clue on how to develop these tests.

The course of REST API has many topics related with the development of this project, and many of these topics are yet relatively new to me: I.e. The concepts of Serializers and Views, Filtering with tags/groups, objects retrieval and the application deployment, and I think these are essencial subjects to continue the development of this technical test.

Unfortunatly there was not enough time for me to attend for these classes before the deadline of this test, although I can figure out they will be very useful.