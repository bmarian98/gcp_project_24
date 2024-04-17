# DevOps Flow on GCP for Flask Application

### Project Overview

This project deploys a simple __*Flask*__ web application on __*Google Kubernetes Engine*__ (__GKE__) with a single route (__/__). The route displays the tier/branch and container hostname. The application leverages a three-branch development model (__dev, qa, main__) and a CI/CD pipeline managed by Cloud Build.

### Development Workflow

__Branching__: Create a feature branch from the dev branch for development.
__Development__: Implement your application logic and commit code to the feature branch.
Push to Repository: Push the feature branch to your version control system (e.g., Git).
CI/CD Pipeline: The push triggers Cloud Build's automated pipeline.
Build and Push Image: Cloud Build executes the __*cloudbuild.yaml*__ file, which:
- Builds a Docker image based on your code.
- Pushes the image to Google Artifact Registry under the appropriate directory: /dev, /qa, or /prod.
- __Deployment__: Cloud Build deploys the image as a Kubernetes deployment with two replicas to the designated namespace (dev, qa, or prod) determined by the _BUILD_DEPLOY_NAME environment variable set during trigger creation.

__Testing and Merge__:
Access the deployed application in the corresponding environment to verify functionality.
Once testing is complete, merge the feature branch into qa for further testing.
After successful QA, merge the code into main (production) for final deployment.

### Environments

- __*Dev*__: Deploys code from the dev branch for development and initial testing.
- __*QA*__: Deploys code from the qa branch for rigorous quality assurance.
- __*Prod (Main)*__: Deploys code from the main branch to the production environment.
Key Benefits

__Automated Deployments__: Cloud Build automates the build, push, and deployment process, ensuring consistency and efficiency across environments.
__Dynamic Targeting__: Deployment targets specific namespaces (dev, qa, or prod) based on the triggered branch, streamlining development and testing.
__Containerization__: GKE provides containerized deployments, offering scalability and portability.
Additional Considerations

__Testing__: Consider integrating unit and integration testing into the CI/CD pipeline for early error detection.
__Monitoring__: Implement continuous monitoring for application performance and health insights.
__Infrastructure as Code (IaC)__: Explore tools like Terraform to manage and automate infrastructure provisioning on GCP.


### Results

In the following images are two different hostname for each environment. This is because there are two replicas for each environment.

- Dev

![dev1](https://github.com/bmarian98/gcp_project_24/assets/39569343/253e1648-1325-4998-bb7c-bb5850d5e3ac)
![dev2](https://github.com/bmarian98/gcp_project_24/assets/39569343/ccac10f0-ca60-4cae-a229-6327970a1dec)

- Qa

![qa1](https://github.com/bmarian98/gcp_project_24/assets/39569343/fe95d5d3-b76f-4b42-882c-619f2946e326)
![qa2](https://github.com/bmarian98/gcp_project_24/assets/39569343/83a343bc-d470-4dd0-bd45-951af4adb229)

- Prod

![prod1](https://github.com/bmarian98/gcp_project_24/assets/39569343/0484513c-5995-4fbe-abc3-c344f9e4687b)
![prod2](https://github.com/bmarian98/gcp_project_24/assets/39569343/90eaa0c9-3416-401e-849d-4da18e75668b)