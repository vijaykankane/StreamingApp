FROM node:18-alpine

WORKDIR /app

# Copy only package files for caching
COPY streamingService/package*.json ./streamingService/


# Install service dependencies
WORKDIR /app/streamingService
RUN npm install --production

# Copy actual source code
WORKDIR /app
COPY streamingService ./streamingService
COPY common ./common

# Run service
WORKDIR /app/streamingService
EXPOSE 3002
CMD ["npm", "run", "start"]
