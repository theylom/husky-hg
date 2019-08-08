# tdog-husky-hg 

> Git / Mercurial hooks made easy.
>
> `tdog-husky-hg` is a fork of `husky-hg`.
> The only difference is, that it is a custom validator.
>

Husky can prevent bad commit.

## Install

```sh
npm install tdog-husky-hg --save-dev
```

```sh
yarn add tdog-husky-hg --dev
```

```bash
git commit -m "Keep calm and commit"
```

_Existing hooks aren't replaced and you can use [any git/Mercurial hook](HOOKS.md)._

_If you're migrating from `ghooks`, simply run `npm uninstall ghooks --save-dev && npm install husky --save-dev` and edit `package.json`. Husky will automatically migrate `ghooks` hooks._


## Uninstall

```sh
npm uninstall tdog-husky-hg
```

```sh
yarn remove tdog-husky-hg
```

## Tricks

<details>


### Git GUI clients support

If you've installed Node using the [standard installer](https://nodejs.org/en/), [nvm](https://github.com/creationix/nvm) or [homebrew](http://brew.sh/), Git hooks will be executed in GUI applications.

### Working with multiple version of Node

If [`nvm`](https://github.com/creationix/nvm) is installed, husky will try to use the `default`/`current` installed Node version or use the project `.nvmrc`.

__Tip__ to use the system-installed version of node, `nvm` provides a [`system`](https://github.com/creationix/nvm#system-version-of-node) alias

### Git submodule and subtree support

Yes

### Mercurial subrepo support

No

### Cygwin support

Yes

### Yarn support

Please use `yarn` `v0.24+`

</details>

## License

MIT
