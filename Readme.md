
# Project Title

##  Brand Intelligence System
The AI Brand Intelligence System is an advanced tool designed to gather, analyze, and present real-time information about companies' brands from various online sources. By leveraging multiple data sources like Reddit, open news APIs, and FAISS Vectorstore, this system provides dynamic insights that help users understand the public perception, trends, and updates surrounding a brand.

### Key Fetures:
* Data Collection: The system fetches real-time data from diverse sources including Reddit, news outlets, and other open APIs, ensuring a comprehensive and up-to-date view of the brand.
* FAISS Vectorstore Integration: Using FAISS, a fast similarity search engine, the system processes and embeds PDFs (e.g., reports, whitepapers, or case studies), enabling easy search and retrieval of brand-related information.
* Brand Insights: The system processes and analyzes textual data to generate insightful summaries, sentiment analysis, and trends based on the latest content available.
* Embeddings: Natural Language Processing (NLP) techniques are employed to generate meaningful embeddings from documents, allowing for effective content matching and brand tracking.

### Setup
* project hirearchy
    | backend: backend code built on fastAPI
    | frontent: frontend code on built on nextjs
    | cloudformation: contains cloudformation yamls for infra setup

* Backend setup:
    - create python environment:
        - Download conda: https://www.anaconda.com/products/distribution
        - Install conda GUI
        - List env: conda env list
        - Create condo environment: conda create --name fair-ai-env python=3.10
        - Activate env: conda activate fair-ai-env
        - Install dependencies: \
            ```
            cd backend \
            pip install -r requirements.txt </code>
            ```
        - Add needed environment vairbles: in .env
            ```
            MISTRAL_KEY=
            CLAUDE_KEY=
            REDDIT_CLIENT_ID=
            REDDIT_CLIENT_SECRET=
            USER_AGENT=langgraphagent
            ASK_NEWS_ID=
            ASK_NEWS_SECRET=
            ```
        - Run the code:
        ```
        python main.py [OR] uvicorn main:app
        ```
* Frontend Setup:
    - Follow the steps:
        ```
        sudo apt-get install -y curl
        curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh
        sudo bash nodesource_setup.sh
        sudo apt-get install -y nodejs
        npm install
        npm run dev
        ```
* Infra Setup:
    - Create a ecr repo with names:
        - backend
        - frontend
    - Create docker images for frontend
        ```
        cd frontend
        docker buildx build --platform linux/amd64 -f Dockerfile --no-cache -t 430957151316.dkr.ecr.us-west-2.amazonaws.com/frontend:v1.0.3 .
        aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 430957151316.dkr.ecr.us-west-2.amazonaws.com
        docker push  430957151316.dkr.ecr.us-west-2.amazonaws.com/frontend:v1.0.3
        ```
    - Create docker images for backend
        ```
        cd backend
        docker buildx build --platform linux/amd64 -f Dockerfile --no-cache -t 430957151316.dkr.ecr.us-west-2.amazonaws.com/backend:v1.0.3 .
        aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 430957151316.dkr.ecr.us-west-2.amazonaws.com
        docker push  430957151316.dkr.ecr.us-west-2.amazonaws.com/backend:v1.0.3
        ```
    - Run the infra code:
        [Note] Modify the parameters/varibales if needed
        ```
        cd cloudformation
        aws cloudformation create-stack --stack-name ecs-stack --template-body file://ecs-infra.yaml

        ```
    - Resource Created:
        - ALBListenerHTTP = AWS::ElasticLoadBalancingV2::Listener
        - AppCloudwatchLogsGroup = AWS::Logs::LogGroup
        - BackendService = AWS::ECS::Service
        - BackendTd = AWS::ECS::TaskDefinition
        - BrandALB = AWS::ElasticLoadBalancingV2::LoadBalancer
        - ECSCluster = AWS::ECS::Cluster
        - FairUiService = AWS::ECS::Service
        - TargetGroup = AWS::ElasticLoadBalancingV2::TargetGroup
        - UiTd = AWS::ECS::TaskDefinition
