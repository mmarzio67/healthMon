<template>
  <section>
    <h1>Edit sportactivity</h1>
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
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditSportactivity',
  props: ['id'],
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    this.GetSportactivity();
  },
  computed: {
    ...mapGetters({ sportactivity: 'stateSportactivity' }),
  },
  methods: {
    ...mapActions(['updateSportactivity', 'viewSportactivity']),
    async submit() {
    try {
      let sportactivity = {
        id: this.id,
        form: this.form,
      };
      await this.updateSportactivity(sportactivity);
      this.$router.push({name: 'Sportactivity', params:{id: this.sportactivity.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetSportactivity() {
      try {
        await this.viewSportactivity(this.id);
        this.form.title = this.sportactivity.title;
        this.form.content = this.sportactivity.content;
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
});
</script>
