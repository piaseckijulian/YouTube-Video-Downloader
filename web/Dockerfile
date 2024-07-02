FROM node:20-bullseye-slim

RUN npm install -g pnpm

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN pnpm i --frozen-lockfile

COPY . .

EXPOSE 5173

CMD pnpm dev --host