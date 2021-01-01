<template>
  <div>
    <beat-loader v-if="loading"></beat-loader>
    <div v-if="{{table.object}}.msg" xs12>\{ {{table.object}}.msg \}
    <div v-if="isRequest">
        <{{table.class}}Form></{{table.class}}Form>
    </div>
    <div v-else>
    <v-data-table
      title="{{table.title}}"
      :items="response.data"
      :headers="headers"
    ></v-data-table>
    </div>
  </div>
</template>

<script>
import {{group}}Service from "@/services/{{group}}Service";
import BeatLoader from "@/components/common/Spinner.vue";

export default {
  value: "{{table.class}}",
  components: {
    BeatLoader,
  },
  props: [],
  data() {
    return {
      loading: true,
      response: {
        rc: 0,
        msg: null,
        data: []
      },
      {{ table.object }}: {},
      headers: [
      {% for col in table.columns %}{% if loop.index > 1 %}, {% endif %}{ id: {{  loop.index }}, value: '{{ col }}', text: '{{ table.labels[loop.index-1] }}' }
      {% endfor %}
      ],
    };
  },
  computed: {},
  mounted() {},
  methods: {
    async get{{ table.class}}() {
        this.loading = true;
        this.response = await get{{ group }}Service();
        this.loading = false;
    }
  },
  created() {},
};
</script>
<style scoped>
</style>