<template>
  <div>
    <section>
      <h1>Add new sport activity</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Sport activities</h1>
      <hr/><br/>

      <div v-if="sportactivities.length">
        <div v-for="sportactivity in sportactivities" :key="sportactivity.id" class="notes">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Sport activity Title:</strong> {{ sportactivity.title }}</li>
                <li><strong>Athlete:</strong> {{ sportactivity.athlete.username }}</li>
                <li><router-link :to="{name: 'Sportactivity', params:{id: sportactivity.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'DashboardView',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getSportactivities');
  },
  computed: {
    ...mapGetters({ sportactivities: 'stateSportactivities'}),
  },
  methods: {
    ...mapActions(['createSportactivity']),
    async submit() {
      await this.createSportactivity(this.form);
    },
  },
});
</script>
