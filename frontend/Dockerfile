# Step 1: Build the React app using Node.js
FROM node:20.0.0-alpine AS build
# Step 1: Build the Next.js app using Node.js
# FROM node:18.13.0-alpine AS build

# Set working directory inside the container
WORKDIR /app

# Set the environment to 'production'
ENV NODE_ENV=dev

# Copy the package.json and package-lock.json files
COPY package.json /app/

# Install dependencies (using npm)
RUN npm install

# Copy the rest of the frontend application code
COPY . /app/

EXPOSE 3000
# Command to start the Node.js server
CMD ["npm", "run", "dev"] 
# Build the Next.js app for production
# RUN npm run build  # This generates the .next folder

# # Step 2: Serve the Next.js app using nginx or next server

# # Use nginx to serve the app, or you can run the Next.js app using its built-in server
# FROM nginx:alpine

# # Copy the built Next.js app from the build stage
# COPY --from=build /app/.next /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/nginx.conf

# # Expose port 80 for the frontend
# EXPOSE 80

# # Start nginx server to serve the Next.js app
# CMD ["nginx", "-g", "daemon off;"]
