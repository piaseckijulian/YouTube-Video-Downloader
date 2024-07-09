FROM node:20-bullseye-slim

RUN npm install -g pnpm

WORKDIR /app

COPY package.json .

RUN pnpm i

COPY . .

ENV API_URL=http://api:5000

EXPOSE 5173

CMD ["pnpm", "dev", "--host"]