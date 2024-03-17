<script>
  import { Router, Route, Link } from 'svelte-navigator'
  import Glav from './glav.svelte'
  import Onas from './onas.svelte'
  import Svize from './svize.svelte';
  import Astrologimap from './Astrologimap.svelte';
  import Astrologi from './Astrologi.svelte';
  import ChildNumerology from './ChildNumerology.svelte';
  import AllAboutYou from './AllAboutYou.svelte';
  import Sovmestimost from './Sovmestimost.svelte';
  import SolarYear from './SolarYear.svelte';

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

    <Route path='/Astrologi'>
      <Astrologi/>
    </Route>

    <Route path='/AllAboutYou'>
      <AllAboutYou/>
    </Route>

    <Route path='/ChildNumerology'>
      <ChildNumerology/>
    </Route>

    <Route path='/Sovmestimost'>
      <Sovmestimost/>
    </Route>

    <Route path='/SolarYear'>
      <SolarYear/>
    </Route>

  </Router>
</main>

<style>
</style>
