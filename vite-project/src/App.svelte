<script>
  import { Router, Route, Link } from 'svelte-navigator'
  import Glav from './glav.svelte'
  import Onas from './onas.svelte'
  import Svize from './svize.svelte';
  import Astrologimap from './Astrologimap.svelte';

</script>

<main>
  
  <Router>

    <Route path='/'>
      <Glav/>
    </Route>

    <Route path='/Onas'>
      <Onas/>
    </Route>

    <Route path='/Sviz'>
      <Svize/>
    </Route>

    <Route path='/Astrologimap'>
      <Astrologimap/>
    </Route>

  </Router>
</main>

<style>
</style>
