import paddlehub as hub

module = hub.Module(name="stable_diffusion")
text = input("Enter the prompt : ")
text_prompts = [text]
file_name = text.replace(" ", "_")
filename = filename[:50]
da = module.generate_image(text_prompts=text_prompts, batch_size=1, output_dir='./stable_diffusion_out/')
da[0].chunks[-1].chunks.plot_image_sprites(skip_empty=True, show_index=True, keep_aspect_ratio=True)
da[0].chunks[-1].chunks.save_gif(f'{filename}-pg.png')
da[0].chunks[0].chunks.plot_image_sprites(skip_empty=True, show_index=True, keep_aspect_ratio=True)
da[0].chunks[0].chunks.save_gif(f'{filename}-result.png')
