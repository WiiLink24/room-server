# The Underground
This folder assists with building CSS for The Underground.

While its main implementation is within the `templates/` directory, CSS is built and minified here.
It makes usage of the [Bulma](https://bulma.io) CSS framework, along with [Font Awesome](https://fontawesome.com).

To avoid large build times, a pre-built version of CSS (embedding fonts) is included. It is generated via [esbuild](https://esbuild.github.io).

If making changes or updating, please run `yarn build` so that `output/app.css` is present.