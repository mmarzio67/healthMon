import axios from "axios";

const instance = axios.create({
  baseURL:
    //"https://vuejs-udemy-max-default-rtdb.europe-west1.firebasedatabase.app",
    //"https://identitytoolkit.googleapis.com/v1",

    "http://localhost:5000/"
    
});

//instance.defaults.headers.common["SOMETHING"] = "something";

export default instance;
