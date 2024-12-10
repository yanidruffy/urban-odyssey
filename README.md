# Urban Odyssey
<a name="top"></a><br>

![Urban Odyssey](./docs/readme_images/amiresponsive.png)

## Description

Welcome to Urban Odyssey, your go-to platform for stylish, durable, and minimalist everyday carry solutions. We partner with leading brands like Aer, Peak Design, and tomtoc to empower digital nomads and adventurers with products that combine innovation and style.

This project was developed as part of Code Institute's Full Stack Software Developer program.

## Live Demo

**Check out the live website here:** [Urban Odyssey!](https://urban-odyssey-d9c0f3df42fe.herokuapp.com/)

## Project Management

### Project Board

[Notion](https://www.notion.so/) is the application I used to work on my [Project Board](https://www.notion.so/Urban-Odyssey-12a9d8c205da8089a485cf101b551234?pvs=4) using an agile approach.

[Back to Top](#top)

## Design Choices

### Color Scheme

To maintain simplicity and a minimalist aesthetic, he primary color scheme for the site is black and white. I also used Bootstrap’s default colors to maintain consistency with the design patterns. These colors help to create a clean interface and incorporating an urban vibe.

<details>
<summary><strong>Color Palette</strong></summary>

![Color Palette by Coolors](./docs/readme_images/color-palette.png)

</details>

### Typography

I used **Montserrat**, a modern sans-serif font, throughout the site. Its clean lines and readable design fit the overall minimalist theme.

[Back to Top](#top)

## Deployment

**Urban Odyssey** was deployed using [Heroku](https://www.heroku.com/) and is built upon a template from [Code Institute](https://github.com/Code-Institute-Org/ci-full-template).

### 1. Heroku Setup
1. Create an account on [Heroku](https://www.heroku.com/) if you don't already have one.
2. After logging in, click **New** in the dashboard and select **Create new app**.
3. Enter a unique app name, choose your region, and click **Create App**.

<details>
<summary><strong>Heroku Setup</strong></summary>

![Heroku Start Deployment Example](./docs/readme_images/deployment-start.png)
![Create App Form Deployment](./docs/readme_images/deployment-start-steps.png)

</details>

### 2. Connecting to a GitHub Repository
1. Navigate to the **Deploy** tab of your Heroku app.
2. Under **Deployment method**, select **GitHub**.
3. Authenticate and search for your repository name, then click **Connect**.

<details>
<summary><strong>Connect GitHub Repository</strong></summary>

![Connect GitHub Example](./docs/readme_images/deployment-github-connect.png)

</details>

### 3. Configuring Environment Variables
1. Navigate to the **Settings** tab in your Heroku app dashboard.
2. Click **Reveal Config Vars** to add the necessary environment variables.
3. Include all required variables for your application, such as:
   - Database connection details.
   - Secret keys for your framework and third-party services.
   - API keys for payment processors and media storage providers.

Ensure that each variable corresponds to a value defined in your project's settings and `.env` file in order for the application to function properly.

### 4. Adding Buildpacks
1. Scroll down in the **Settings** tab to the **Buildpacks** section.
2. Add the following buildpack:
   - `python`

<details>
<summary><strong>Adding Buildpacks</strong></summary>

![Buildpacks Example](./docs/readme_images/deployment-buildpack.png)

</details>

### 5. Deploying the Application
1. In the **Deploy** tab, scroll to **Manual Deploy**.
2. Select your branch (e.g., `main`) and click **Deploy Branch**.
3. Optionally, enable **Automatic Deploys** for continuous deployment.

<details>
<summary><strong>Manual Deployment</strong></summary>

![Manual Deployment Example](./docs/readme_images/deployment-branch.png)

</details>

### 6. Finalizing Deployment
1. After deployment, you’ll see a success message with a **View** button.
2. Click **View** to visit your live site.

<details>
<summary><strong>Deployment Success</strong></summary>

![Deployment Success Example](./docs/readme_images/deployment-success.png)

</details>
