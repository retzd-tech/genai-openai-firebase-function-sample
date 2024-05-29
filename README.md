# Generative AI on Cloud Function example project

Welcome to the Generative AI with Cloud Functions repository! This project demonstrates how to build a serverless AI application using Firebase Cloud Functions, LangChain, and OpenAI's language model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains the code and instructions for deploying a generative AI application using Firebase Cloud Functions. By leveraging LangChain and OpenAI's language model, the application provides a seamless and scalable solution for generating AI-powered content and responses.

## Features

- **Serverless Architecture**: Utilize Firebase Cloud Functions for a scalable and cost-effective deployment.
- **Generative AI**: Integrate OpenAI's language model to generate human-like text.
- **Modular Design**: Use LangChain for managing and chaining multiple AI model responses.
- **Real-time Functionality**: Automatically trigger AI functions in response to specific events or HTTP requests.

## Architecture

The architecture of this project consists of the following components:

1. **Firebase Cloud Functions**: Handles the serverless deployment and execution of AI functions.
2. **LangChain**: Manages the flow of data and chaining of AI model responses.
3. **OpenAI Language Model**: Generates the content and responses based on input data.

## Setup

Follow these steps to set up and deploy the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/retzd-tech/generative-ai-cloud-functions.git
    cd generative-ai-cloud-functions
    ```

2. **Install Firebase CLI**:
    ```bash
    npm install -g firebase-tools
    ```

3. **Login to Firebase**:
    ```bash
    firebase login
    ```

4. **Initialize Firebase in your project**:
    ```bash
    firebase init
    ```
    - Select **Functions**.
    - Choose your Firebase project.
    - Use the default options for other settings.

5. **Install dependencies**:
    ```bash
    cd functions
    npm install
    ```

6. **Set up OpenAI API key**:
    - Create a `.env` file in the `functions` directory.
    - Add your OpenAI API key:
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        ```

7. **Deploy Firebase functions**:
    ```bash
    firebase deploy --only functions
    ```

## Usage

To use the deployed functions, you can trigger them via HTTP requests or other Firebase-supported events. For example, to generate text using the OpenAI model, send an HTTP POST request to the corresponding Firebase function URL with the necessary input data.

Example request:
```bash
curl -X POST https://us-central1-your-project-id.cloudfunctions.net/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Once upon a time..."}'
```

## Contributing

We welcome contributions to enhance the functionality and improve the codebase. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with descriptive messages.
    ```bash
    git commit -m "Add new feature"
    ```
4. Push your changes to your forked repository.
    ```bash
    git push origin feature-name
    ```
5. Open a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using Generative AI with Cloud Functions! If you have any questions or need further assistance, feel free to open an issue in this repository. Happy coding!
