# # Используйте официальный образ node как базовый
# FROM node:18

# # Установите рабочую директорию в контейнере
# WORKDIR /app

# # Копируйте файл package.json (и package-lock.json, если он есть)
# COPY package*.json ./

# # Установите зависимости приложения
# RUN npm install

# # Копируйте локальные файлы в контейнер
# COPY . .

# # Запустите приложение
# CMD ["npm", "start"]



FROM node:18-alpine as build
WORKDIR /app
COPY package.json /app/package.json
RUN npm install --only=prod
COPY . /app
RUN npm run build
FROM nginx:1.16.0-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]