import api from "@/services/api_service"
import cs from '@/services/common_service'

export default {
    {% for table in tables %}
    async get{{ table.class }}(): {{ table.class }} {
        let resp = await api.getHttpRequest('/{{group}}/{{table.name}}');
        return cs.requestResponse( resp);
    },

    async getA{{ table.class }}( id): {{ table.class }} {
        let resp = await api.getHttpRequest('/{{group}}/{{table.name}}/'+id);
        return cs.requestResponse( resp);
    },

    async post{{ table.class }}( postData:{{ table.class}}) {
        let formData = cs.getFormData( postData)
        let resp = await api.postHttpRequest('/{{group}}/{{table.name}}', formData);
        return cs.requestResponse( resp);
    },
    {% endfor %}
}