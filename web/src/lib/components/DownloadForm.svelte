<script lang="ts">
  import * as Form from '$lib/components/ui/form';
  import { Input } from '$lib/components/ui/input';
  import { formSchema, type FormSchema } from '$lib/schema';
  import LoaderCircle from 'lucide-svelte/icons/loader-circle';
  import {
    superForm,
    type Infer,
    type SuperValidated
  } from 'sveltekit-superforms';
  import { zodClient } from 'sveltekit-superforms/adapters';

  export let data: SuperValidated<Infer<FormSchema>>;

  const form = superForm(data, {
    validators: zodClient(formSchema)
  });

  const { form: formData, enhance, delayed } = form;
</script>

<form method="POST" use:enhance>
  <Form.Field {form} name="videoUrl">
    <Form.Control let:attrs>
      <Input
        {...attrs}
        placeholder="Video URL"
        autocomplete="off"
        bind:value={$formData.videoUrl}
      />
    </Form.Control>

    <Form.FieldErrors />
  </Form.Field>

  <Form.Button class="mt-5 w-full" disabled={$delayed}>
    {#if $delayed}
      <LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
      Downloading
    {:else}
      Download
    {/if}
  </Form.Button>
</form>
