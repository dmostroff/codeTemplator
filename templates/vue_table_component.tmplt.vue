<template>
  <div>
    <beat-loader v-if="loading"></beat-loader>
    <div v-if="{{table.object}}.msg" xs12>\{ {{table.object}}.msg \}</div>
    <div v-else>
    <v-data-table
      title="{{table.title}}"
      :items="response.data"
      :headers="headers"
    ></v-data-table>
    </div>
    <v-dialog v-model="dialogDetail">
      <{{table.class}}Detail
        :{{table.object}Id="{{table.object}}Id"
        @editClientPersonForm="edit{{table.class}}Form"
        @cancel{{table.class}}Detail="cancel{{table.class}}Detail"
      ></{{table.class}}Detail>
    </v-dialog>
    <v-dialog v-model="dialogDetailEdit">
      <{{table.class}}Form
        :a{{table.object}}="{{table.object}}"
        @cancel{{table.class}}Form="cancel{{table.class}}Form"
        @saveForm="saveForm"
      ></{{table.class}}Form>
    </v-dialog>
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
        this.response = await {{group}}Service.get{{ table.class }}();
        this.loading = false;
    }
  },
  created() {},
};
</script>
<style scoped>
</style>