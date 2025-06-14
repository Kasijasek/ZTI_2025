FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN apk update && apk upgrade && npm install

COPY . .

EXPOSE 8001
CMD ["npm", "start"]
