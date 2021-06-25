<template>
<v-form>
  <v-card>
    <v-card-title class="primary white--text">
      {{table.title}}
    </v-card-title>
    <v-card-text>
      <v-container>
        {% for col in table.columns %}<v-row>
            {% if loop.index == 1 %}
              <v-col cols="2" class="caption">
                Id: {{'{{'}}{{table.object}}.id {{'}}'}}
                </v-col>
              <v-spacer></v-spacer>
              <v-col cols="3" class="caption">
                Recorded on: {{'{{'}} formatDateTime({{table.object}}.recorded_on) {{'}}'}}
              </v-col>
            {% else %}
            <v-col cols="2">
            <v-text-field
              v-model="{{table.object}}.{{ col }}"
              label="{{table.labels[loop.index-1]}}"
              :readonly="isReadOnly"
              >
            </v-text-field>
          </v-col>{% endif %}
        </v-row>{% endfor %}
      </v-container>
    </v-card-text>
    <v-card-actions>
      <EditSaveCancelBtn
        :isReadOnly="isReadOnly"
        @editForm="editForm"
        @saveForm="saveForm"
        @cancelForm="cancelForm"
        @closeForm="closeForm"
      ></EditSaveCancelBtn>
    </v-card-actions>
  </v-card>
  </v-form>
</template>

<script>
import commonService from "@/services/commonService";
// import admService from '@/services/admService'
import {{table.object}}Service from "@/services/{{table.object}}Service";
import EditSaveCancelBtn from "@/components/common/EditSaveCancelBtn";

export default {
  value: "{{table.class}}",
  components: {
    EditSaveCancelBtn
  },
  props: {
    {{table.object}}: Object,
  },
  data() {
    return {
      isReadOnly: true,
    };
  },
  computed: {},
  mounted() {
    this.prev{{table.class}} = commonService.clone( this.{{table.object}})
  },
  methods: {
    formatDateTime(datetime) {
      return commonService.formatDateTime(datetime);
    },
    editForm() {
      this.isReadOnly = false
    },
    async saveForm() {
      let {{table.object}} = await {{table.object}}Service.post{{table.class}}(this.{{table.object}})
      this.isReadOnly = true
      this.$emit("saveForm", {{table.object}});
    },
    cancelForm() {
      this.isReadOnly = true
      this.{{table.object}} = commonService.clone( this.prev{{table.class}})
    },
    closeForm() {
      this.$emit("cancelForm")
    },
  },
  created() {},
};
</script>
<style scoped>
</style>