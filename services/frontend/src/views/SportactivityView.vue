<template>
  <div v-if="sportactivity">
    <p><strong>Title:</strong> {{ sportactivity.title }}</p>
    <p><strong>Content:</strong> {{ sportactivity.content }}</p>
    <p><strong>Athlete:</strong> {{ sportactivity.athlete.username }}</p>

    <div v-if="user.id === sportactivity.athlete.id">
      <p><router-link :to="{name: 'EditSportactivity', params:{id: sportactivity.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeSportactivity()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'SportactivityView',
  props: ['id'],
  async created() {
    try {
      await this.viewSportactivity(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ sportactivity: 'stateSportactivity', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewSportactivity', 'deleteSportactivity']),
    async removeSportactivity() {
      try {
        await this.deleteSportactivity(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
