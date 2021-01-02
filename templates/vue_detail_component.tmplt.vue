<template>
  <v-card>
    <v-card-header :md-elevation="2">
      {{table.title}}
    </v-card-header>
    <v-card-text>
      <v-container>
        {% for col in table.columns %}<v-row>
          <v-col><span class="subtitle-2">{{ table.labels[loop.index-1] }}</span>:</v-col>
          <v-col>
            {{ '{{' }}{{table.object}}.{{ col }}{{ '}}' }}
          </v-col>
        </v-row>{% endfor %}
      </v-container>
    </v-card-text>
    <v-card-actions md-alignment="right">
      <v-btn @click="editForm">Edit</v-btn>
      <v-btn @click="cancelForm">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  value: "{{table.class}}",
  components: {
  },
  props: {
    {{table.object}}: Object
  },
  data() {
    return {
    };
  },
  computed: {},
  mounted() {},
  methods: {
    editForm() {
      this.$emit( "edit{{table.class}}Form" )
    },
    cancelForm() {
      this.$emit( "cancel{{table.class}}Form" )
    }
  },
  created() {},
};
</script>
<style scoped>
</style>