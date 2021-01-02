<template>
<v-form>
  <v-card>
    <v-card-header :md-elevation="2">
      {{table.title}}
    </v-card-header>
    <v-card-text>
      <v-container>
        {% for col in table.columns %}<v-row>
          <v-col cols="12" md="4">
            {% if loop.index == 1 %}
            <span class="caption">{{table.labels[loop.index-1]}}</span>
            <span class="">{{'{{'}}{{ table.object }}.{{col}} {{'}}'}}</span>
            {% else %}<v-text-field>
              v-model="{{table.object}}.{{ col }}"
              label="{{table.labels[loop.index]}}"
            </v-text-field>
            {% endif %}
          </v-col>
        </v-row>{% endfor %}
      </v-container>
    </v-card-text>
    <v-card-actions md-alignment="right">
      <v-btn @click="editForm">Edit</v-btn>
      <v-btn @click="cancelForm">Cancel</v-btn>
    </v-card-actions>
  </v-card>
  </v-form>
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