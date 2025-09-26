import axios from "axios"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// TODO: Figure out how to have API bypass auth

api.interceptors.request.use(
    (config) => {
        return config
    },
)

export default api