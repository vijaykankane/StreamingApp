FROM node:18

# Root app folder
WORKDIR /app

# Copy chatService package.json
COPY chatService/package*.json ./chatService/

# Install deps
WORKDIR /app/chatService
RUN npm install

# Copy chatService files
COPY chatService/. .

# Copy common folder correctly (THIS FIXES THE ISSUE)
WORKDIR /app
COPY common ./common
ENV NODE_ENV=production
EXPOSE 3002

WORKDIR /app/chatService

CMD ["npm", "run", "start"]


