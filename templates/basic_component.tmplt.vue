<template>
  <div>
    <beat-loader v-if="loading"></beat-loader>
    <data-table
      v-else
      title="Merchants"
      :items="merchants"
      :headers="columns"
    ></data-table>
  </div>
</template>

<script>
import ptpeService from "@/services/ptpeService";
import BeatLoader from "@/components/common/Spinner.vue";
import DataTable from "@/components/common/DataTable.vue";

export default {
  value: "PtpeMerchants",
  components: {
    BeatLoader,
    DataTable,
  },
  props: [],
  data() {
    return {
      loading: true,
      items: [],
      resp: {
          rc: 0,
          msg: '',
          data: []
      },
      {{ headers }}
    };
  },
  computed: {},
  mounted() {},
  methods: {},
  created() {
      async get() {
    this.resp = await {{group}}Service.gets();
    }

  },
};
</script>
<style scoped>
div.make-scrollable {
  height: 600px;
  overflow-y: scroll;
}
</style>