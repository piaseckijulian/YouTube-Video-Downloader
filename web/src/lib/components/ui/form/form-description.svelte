<script lang="ts">
  import { cn } from "$lib/utils.js"
  import * as FormPrimitive from "formsnap"

  let className: string | undefined | null = undefined
  export { className as class }
</script>

<FormPrimitive.Description
  class={cn("text-muted-foreground text-sm", className)}
  {...$$restProps}
  let:descriptionAttrs
>
  <slot {descriptionAttrs} />
</FormPrimitive.Description>
