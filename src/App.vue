<template>
  <div class="container">
    <h1 class="title">Filter LeetCode Questions Instantly</h1>
    <h3 class="sub-heading">Fast, Optimized, No API Calls</h3>
    <p class="author">Built by Rohit Singh</p>
    <div class="filter-buttons">
      <div class="dropdown" ref="tagsDropdown">
        <button @click="toggleDropdown('tags')" class="dropdown-button">
          Tags <span>{{ showTags ? '▲' : '▼' }}</span>
        </button>
        <div v-if="showTags" class="dropdown-content scrollable-tags">
          <label
            v-for="(value, tag) in otherTags"
            :key="tag"
            class="tag-option"
          >
            <input type="checkbox" :value="value" v-model="selectedTags" />
            {{ tag }}
          </label>
        </div>
      </div>
      <div class="dropdown" ref="difficultyDropdown">
        <button @click="toggleDropdown('difficulty')" class="dropdown-button">
          Difficulty <span>{{ showDifficulty ? '▲' : '▼' }}</span>
        </button>
        <div v-if="showDifficulty" class="dropdown-content">
          <label
            v-for="(value, tag) in difficultyTags"
            :key="tag"
            :class="['tag-option', tag.toLowerCase()]"
          >
          <input
            type="checkbox"
            :value="value"
            :checked="selectedTags.includes(value)"
            @change="selectOnlyThisDifficulty(value)" />
            {{ tag }}
          </label>
        </div>
      </div>
    </div>
    <div class="selected-filters" v-if="selectedTags.length > 0">
      <span
        v-for="tag in selectedTags"
          :key="tag"
          class="filter-chip">
            {{ getTagName(tag) }}
          <button class="remove-btn" @click="removeTag(tag)">×</button>
      </span>
    </div>


    <div class="questions" @scroll="onScroll" ref="questionContainer">
      <h2>Filtered Questions:</h2>
      <ul>
        <li v-for="(question, index) in visibleQuestions" :key="index">
          <div class="question-item">
            <span class="question-number">
              {{ (questionList.indexOf(question) + 1).toString().padStart(4, ' ') }}.
            </span>
            <a
            :href="generateLeetcodeUrl(question.name)"
            target="_blank"
              rel="noopener noreferrer"
              class="question-link">
              {{ question.name }}
            </a>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { tagDict, questionList } from './components/data.js';

export default {
  data() {
    return {
      visibleCount: 50,
      tagDict,
      questionList,
      selectedTags: [],
      showDifficulty: false,
      showTags: false
    };
  },
  computed: {
    visibleQuestions() {
  return this.filteredQuestions.slice(0, this.visibleCount);
},
filteredQuestions() {
  const result =
    this.selectedTags.length === 0
      ? this.questionList
      : this.questionList.filter((q) =>
          this.selectedTags.every((tag) => q.tags.includes(tag))
        );
  this.$nextTick(() => {
    this.visibleCount = 50;
  });
  return result;
},

    difficultyTags() {
      return Object.fromEntries(
        Object.entries(this.tagDict).filter(([tag]) =>
          ["Easy", "Medium", "Hard"].includes(tag)
        )
      );
    },
    otherTags() {
      return Object.fromEntries(
        Object.entries(this.tagDict).filter(([tag]) =>
          !["Easy", "Medium", "Hard"].includes(tag)
        )
      );
    }
  },
  methods: {
    getTagName(tagValue) {
  const entry = Object.entries(this.tagDict).find(([_, val]) => val === tagValue);
  return entry ? entry[0] : '';
},
removeTag(tagValue) {
  this.selectedTags = this.selectedTags.filter(tag => tag !== tagValue);
},

    selectOnlyThisDifficulty(value) {
  const difficultyValues = Object.values(this.difficultyTags);

  // If the value is already selected, unselect all difficulties
  if (this.selectedTags.includes(value)) {
    this.selectedTags = this.selectedTags.filter(tag => !difficultyValues.includes(tag));
  } else {
    // Else, remove all difficulties and add the selected one
    this.selectedTags = this.selectedTags.filter(tag => !difficultyValues.includes(tag));
    this.selectedTags.push(value);
  }
},

    onScroll() {
  const container = this.$refs.questionContainer;
  if (container.scrollTop + container.clientHeight >= container.scrollHeight - 10) {

    if (this.visibleCount < this.filteredQuestions.length) {
      this.visibleCount += 50;
    }
  }
},

    generateLeetcodeUrl(questionName) {
      return `https://leetcode.com/problems/${questionName
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/(^-|-$)/g, "")}/`;
    },
    toggleDropdown(type) {
      if (type === "difficulty") {
        this.showDifficulty = !this.showDifficulty;
        this.showTags = false;
      } else if (type === "tags") {
        this.showTags = !this.showTags;
        this.showDifficulty = false;
      }
    },
    handleClickOutside(event) {
      const difficultyDropdown = this.$refs.difficultyDropdown;
      const tagsDropdown = this.$refs.tagsDropdown;
      if (
        !difficultyDropdown.contains(event.target) &&
        !tagsDropdown.contains(event.target)
      ) {
        this.showDifficulty = false;
        this.showTags = false;
      }
    }
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeDestroy() {
    document.removeEventListener("click", this.handleClickOutside);
  }
};
</script>