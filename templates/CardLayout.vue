<template>
  <div
    class="md-layout md-gutter-small md-alignment-center-center div-card-mat"
  >
    <div class="md-layout-item md-size-90">
      <v-card style="background-color: coral">
        <v-card-header :md-elevation="2">
          <slot name="header"></slot>
        </v-card-header>
        <v-card-text>
          <slot name="content"></slot>
        </v-card-text>
        <v-card-actions md-alignment="right">
          <slot name="action"></slot>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardLayout',
  components: {},
  props: [],
  data () {},
  computed: {},
  mounted () {},
  methods: {}
}
</script>