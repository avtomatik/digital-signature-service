FROM node:18

WORKDIR /frontend

COPY frontend/ /frontend/

RUN npm install

EXPOSE 3000

CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]
