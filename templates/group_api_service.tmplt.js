import api from "@/services/api_service"
import cs from '@/services/common_service'

export default {
    {% for table in tables %}
    async get{{ table.class }}() {
        let resp = await api.getHttpRequest('/{{group}}/{{table.name}}');
        return cs.requestResponse( resp);
    },

    async get{{ table.class }}By{{group_name}}Id( {{group}}_id) {
        let resp = await api.getHttpRequest('/{{group}}/'+{{group}}_id+'{{table.name}}');
        return cs.requestResponse( resp);
    },

    async get{{ table.class }}ById( id) {
        let resp = await api.getHttpRequest('/{{group}}/{{table.name}}/'+id);
        return cs.requestResponse( resp);
    },

    async post{{ table.class }}( postData) {
        let formData = cs.getFormData( postData)
        let resp = await api.postHttpRequest('/{{group}}/{{table.name}}', formData);
        return cs.requestResponse( resp);
    },
    {% endfor %}
}