FROM node:20-bullseye-slim

RUN npm install -g pnpm

WORKDIR /app

COPY pnpm-lock.yaml .
COPY package.json .

RUN pnpm i

COPY . .

EXPOSE 5173

CMD pnpm dev
